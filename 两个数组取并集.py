from typing import List
def jiaoji(nums1: List,nums2: List):
    nums1.sort()
    nums2.sort()
    nums = set()
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            nums.add(nums1[i])
            i += 1
            j += 1
    return list(nums)
