from task_2_hw1 import merge_sorted_files


file1 = open("file1.txt", "w+")
file1.writelines(["3\n", "8\n", "10\n"])
file1.close()

file2 = open("file2.txt", "w+")
file2.writelines(["1\n", "2\n", "5\n"])
file2.close()


def test_task5():
    assert merge_sorted_files(["file1.txt", "file2.txt"]) == [1, 2, 3, 5, 8, 10]