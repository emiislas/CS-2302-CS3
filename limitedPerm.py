def get_subsets(nums, k):
  target = [None]*k
  get_subsets_helper(nums, target, 0, len(nums)-1, 0, k)
 
def get_subsets_helper(nums, target, start, end, index, k):
    i = start
    if (index == k): 
        for i in range(k): 
            print("[", target[i],end = " ]") 
        print()
        return
     
    while(i <= end and end - i + 1 >= k - index): 
        target[index] = nums[i]
        get_subsets_helper(nums, target, i + 1, end, index + 1, k)
        i += 1

nums = [1,2,3]
k = 2
get_subsets(nums, k)