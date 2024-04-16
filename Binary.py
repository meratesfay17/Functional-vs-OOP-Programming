class Solution:
    def binarysearch(self, arr, n, k):
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2

            # Check if k is present at mid
            if arr[mid] == k:
                return mid

            # If k is greater, ignore left half
            elif arr[mid] < k:
                left = mid + 1

            # If k is smaller, ignore right half
            else:
                right = mid - 1

        # If k is not present in the array
        return -1

# Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 4
position = sol.binarysearch(arr, n, k)
if position != -1:
    print(f"The position of {k} in the array is {position}.")
else:
    print(f"{k} is not present in the array.")
