
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return the indices of two numbers that add up to target.
    BUG: May use the same element twice.
    """
    seen = {}

    for i, num in enumerate(nums):
        seen[num] = i  # BUG: stores current element too early
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

    raise ValueError("No valid pair found")


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3], 6))  # BUG: incorrectly returns [0, 0]
