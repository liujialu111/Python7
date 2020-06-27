from typing import List
def erfen(nums: List,var: int):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] == var:
            return left
        elif nums[right] == var:
            return right
        else:
            mid = (left + right) // 2
            if var < mid:
                right = mid
            elif var > mid:
                left = mid
            else:
                return mid