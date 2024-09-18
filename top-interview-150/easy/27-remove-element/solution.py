class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # remove all instances of val
        while val in nums:
            nums.remove(val)

        #return length
        return len(nums)        
        
