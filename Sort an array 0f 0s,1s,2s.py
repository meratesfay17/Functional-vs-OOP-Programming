class Solution:
    def sort012(self, arr, n):
        low = 0
        high = n - 1
        mid = 0

        while mid <= high:
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

# Example usage:
sol = Solution()
arr = [0, 2, 1, 2, 0]
sol.sort012(arr, len(arr))
print(*arr)  # Output: 0 0 1 2 2
