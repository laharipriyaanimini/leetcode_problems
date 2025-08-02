class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        str1=str(x)
        rev=str1[::-1]
        return str1==rev
        