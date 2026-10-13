class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in range(len(s)):
            if s[i].isalnum():
                result.append(s[i].lower())
        return result == result[::-1]
