from time import time
import multiprocessing
import threading
import subprocess

def get_path_solution_of(cell: (int, int), path):
    return_code = subprocess.call("dummyProject.exe")

    print(f"Done ({cell[0]}, {cell[1]})[{path}]: {return_code} (n. solutions)")

def get_cell_solution_of(cell: (int, int)):

    threads = []
    for i in range(8):
        thread = threading.Thread(target=get_path_solution_of, args=[cell, i])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return True

def main():
    cells = []
    for r in range(0, 5):
        for c in range(r, 5):
            cells.append((r, c))

    print(f"Params ({len(cells)}): ", cells)

    with multiprocessing.Pool() as pool:
        for result in pool.imap_unordered(get_cell_solution_of, cells):
            pass

if __name__ == '__main__':
    start = time()

    main()

    print(f"Finished in {time() - start}s")