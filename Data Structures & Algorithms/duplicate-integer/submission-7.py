class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 1
        if len(dic.keys()) < len(nums):
            return True
        return False
        
        