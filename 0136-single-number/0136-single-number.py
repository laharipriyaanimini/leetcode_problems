class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d1={}
        for ele in  nums:
            if ele in d1:
                d1[ele]=d1[ele]+1
            else:
                d1[ele]=1
        for key,val in d1.items():
            if val==1:
                return key       