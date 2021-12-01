from pathlib import Path

INPUTS_PATH = Path(__file__).parent / "inputs"

def load_input(num):
    with open(INPUTS_PATH / f"{num}.txt") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def nums_to_ints(nums):
    return [int(num) for num in nums]
