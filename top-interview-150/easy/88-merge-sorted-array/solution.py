class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # nums2 has elements that need attention
        if n != 0:

            # there are no elements in nums1 to merge, copy elements over
            if m == 0:
                nums1[:] = nums2
            # merge lists
            else:

                # slice trailing elements
                nums1[:] = nums1[:m]
                
                # combine lists
                nums1.extend(nums2)

                # sort lists
                nums1.sort()
