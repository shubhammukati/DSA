def findMaxProduct(self, arr):
        if n == 1:
		    return arr[0]

    	# Find count of negative numbers, count
    	# of zeros, negative number
    	# with least absolute value
    	# and product of non-zero numbers
    	max_neg = -999999999999
    	count_neg = 0
    	count_zero = 0
    	prod = 1
    	mod=10**9
    	for i in range(len(arr)):
    
    		# If number is 0, we don't
    		# multiply it with product.
    		if arr[i] == 0:
    			count_zero += 1
    			continue
    
    		# Count negatives and keep
    		# track of negative number
    		# with least absolute value.
    		if arr[i] < 0:
    			count_neg += 1
    			max_neg = max(max_neg, arr[i])
    
    		prod = prod * arr[i]
    
    	# If there are all zeros
    	if count_zero == n:
    		return 0
    
    	# If there are odd number of
    	# negative numbers
    	if count_neg & 1:
    
    		# Exceptional case: There is only
    		# negative and all other are zeros
    		if (count_neg == 1 and count_zero > 0 and
    			count_zero + count_neg == n):
    			return 0
    
    		# Otherwise result is product of
    		# all non-zeros divided
    		# by negative number
    		# with least absolute value
    		prod = int(prod / max_neg)
    
    	return prod%mod
