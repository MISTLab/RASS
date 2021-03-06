import csv


FOLDER_RESULTS_DORA_MESH = "../results/physical_dora_mesh"
FOLDER_RESULTS_HOP_COUNT = "../results/physical_hop_count"
FOLDER_RESULTS_STIGMERGY = "../results/physical_stigmergy"
ROBOT_IDS = [1,2,3,5,6]
METRIC = ["storage", "reliability"]


def aggregate_results(folder, metric) -> dict:
    sorted_results = {}

    for robot_id in range(100):
        with open(f"{folder}/{robot_id}_{metric}.csv", "r") as result_file:
            store_sorted_results(csv.reader(result_file), sorted_results)

    return sorted_results


def store_sorted_results(file_reader, sorted_results: dict) -> None:
    next(file_reader)  # Skip header

    for line in file_reader:
        step = line[2]
        run = line[1]

        if run not in sorted_results:
            sorted_results[run] = {}
        
        if step in sorted_results[run]:
            sorted_results[run][step].append(line)
        else:
            sorted_results[run][step] = [line]


def main():
    for folder in [FOLDER_RESULTS_HOP_COUNT, FOLDER_RESULTS_DORA_MESH]:#, FOLDER_RESULTS_HOP_COUNT, FOLDER_RESULTS_STIGMERGY]:
        for metric in METRIC:
            sorted_results = aggregate_results(folder, metric)

            with open(f"{folder}/concatenated_{metric}.csv", "w", newline="") as aggregated_file:
                writer = csv.writer(aggregated_file)
                for run_results in sorted_results.values():
                    for step in run_results.values():
                        for result_line in step:
                            writer.writerow(result_line)
    
                    

if __name__ == "__main__":
    main()
