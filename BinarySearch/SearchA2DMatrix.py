matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def MatrixBsearch(matrix,target,left,right):
            if left>right:
                return False
            mid = (left + right)//2
            if target>=matrix[mid][0] and  target<=matrix[mid][-1]:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            if target > matrix[mid][-1]:
                return MatrixBsearch(matrix,target,mid+1,right)
            elif target <matrix[mid][0]:
                return MatrixBsearch(matrix,target,left,mid-1)
        
    MatrixBsearch(matrix,target,0,len(matrix)-1)
