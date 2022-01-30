
def check_count(nums):
     
    max1=max(nums)
    min1=min(nums)
    count = 0
    for i in nums:
        if i < max1 and i > min1:
            count += 1
    return count

nums = [11,7,2,15,4] 
print(check_count(nums))