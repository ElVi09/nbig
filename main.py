def kbig(nums, k):

    #nums = list(set(nums))
    i = 0
    while i < k:
        a = max(nums)
        nums.remove(a)
        i += 1

    return a
