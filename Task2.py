def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # Record each value of total and num at the end of the loop body.
    return total                        #value of total: 16, num 1

result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body. new list = [4, 9, 2, 1]
    return new_list                    # How does this loop differ from that above? This loop is different because it is creating a new list instead of adding to the value

result = copy([4, 9, 2, 1])

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)                  # Record each value of new_list and value at the end of the loop body. new list: [], [5], [5, 10], value = 2
    return new_list

result = increment_all([4, 9, 2, 1])