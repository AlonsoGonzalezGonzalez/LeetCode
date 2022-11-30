class Solution:
    def containsDuplicate(self, nums):
        duplicates_size=len(nums)
        noDuplicates_size=len(set(nums))
        
        if noDuplicates_size < duplicates_size:
            return True
        return False