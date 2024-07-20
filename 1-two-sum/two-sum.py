class Solution(object):
    def twoSum(self, nums, target):
        map={}
        for i, n in enumerate(nums):
            d=target-n
            if d in map:
                return[map[d],i]
            map[n]=i
        return
        
        