from typing import List


def partition_labels(s: str) -> List[int]:
    """
    rules: divide into most amount of partitions possible where each letter only appears in one partition AT MOST.

    1. for each letter in the string, we will first find the last index it occurs at. We can use a dict(hash map) for this
    because it would just take each letter and re-update it to the new index value when another copy of it appears later.

    2. we will end to keep track of the current partition size along with the last occurring index of the partition.
        - default partition is going to be the first and last occurrence of a letter along with everything in betw.
        - the size value increases by 1 as we traverse thru. the partition to check that all letters fit the rules
        - if a new letter has a lastIndex that is farther down than the current one, we will update the end value.
        - once size value has surpassed end value, we will know that all the values in the current partition follow
        the rules.
    """
    lastIndex = {}
    for i, letter in enumerate(s):
        lastIndex[letter] = i

    result = []
    size, end = 0, 0
    for i, letter in enumerate(s):
        size += 1
        end = max(end, lastIndex[letter])

        if i == end:
            result.append(size)
            size = 0
    return result


# Time Complexity: O(n)     where n is the length of s
# Space Complexity: O(1)    the ds created here will not have more than 26 letters(every letter of alphabet)


print(partition_labels("eccbbbbdec"))
