'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].
Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000

'''
#using Hashmap
from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums2_dict={x:True for x in nums2}
        nums1_diff=[num for num in nums1 if num not in nums2_dict]
        nums1_dict={x:True for x in nums1}

        nums2_diff=[num for num in nums2 if num not in nums1_dict]
        return set(nums1_diff),set(nums2_diff)


#using array

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1_c=nums1.copy()
        n2_c=nums2.copy()
        i = 0
        while i < len(nums1):  # Use len(nums1) to avoid out-of-bounds errors after removal
            if nums1[i] in n2_c:  # If element in nums2, remove from nums1
                 nums1.pop(i)  # Pop removes the element at index i
            else:
                 i += 1  # Only increment if no removal, to maintain correct index
        j=0
        while j<len(nums2):
            if nums2[j] in n1_c:
                nums2.pop(j)
            else:
                 j+=1
    

        return set(nums1),set(nums2)