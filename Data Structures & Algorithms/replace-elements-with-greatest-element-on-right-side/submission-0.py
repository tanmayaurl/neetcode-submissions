class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        var = len(arr)
        for i in range(var-1,-1,-1):
            back = arr[i]
            arr[i] = max_val
            max_val = max(max_val, back)
        return arr