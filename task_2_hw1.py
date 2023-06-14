from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    a = []
    for i in file_list:
        with open(i) as f:
            for line in f.readlines():
                a.append(int(line))
    return sorted(a)