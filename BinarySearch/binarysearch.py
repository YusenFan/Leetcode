nums = [-1,0,3,5,9,12]

target = 4

def bsearch(nums,target,left,right):
    mid = (left + right)//2
    if nums[mid] == target:
        return mid
    if left>right:
        return -1
    elif nums[mid]>target:
        return bsearch(nums,target,left,mid-1)
    else:
        return bsearch(nums,target,mid+1,right)

bsearch(nums,target,0,len(nums)-1)
