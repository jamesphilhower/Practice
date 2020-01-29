# Determine if the number of 1's in 64-bit number is odd (Return True) or even (Return False)

# Go through each bit in the number, flipping result based on the current bit
# Big O N
def first_parity(x: int) -> bool:
    result = False
    while(x):
        result ^= x & 1
        # x & 1, checks to see if the LSB is set to 1
        # ^= toggles a bit whenever right side is true: 
        # 0 && 0 -> 0 
        # 0 && 1 -> 1
        # 1 && 0 -> 1
        # 1 && 1 -> 0
        result >>= 1
        # >>= shift bits to the right one, removing LSB
    return result

# Use a trick to speed up the above that erases lowest set bit and swap based on that
def second_parity(x: int) -> bool:
    result = False
    while(x):
        x &= x-1
        # the above trick "x&(x-1)" works as follows:
        # The lowest bit set in X will be changed to a 0 and all previous will be turned to 1's. 
        # Anding these will yield the lowest bit removed because all the new 1's 
        # will be guarenteed to be paired with 0's 
        result ^= 1
        # Now we toggle result for each bit that is cleared 
    return result


def precompute_parities() -> [bool]:
    return [True if second_parity(number) else False for number in range(2**16)]
    # Cache all 16 bit words as True or False to improve time by up to factor of 16 (all 1's)
        
def third_parity(x: int) -> bool:
    precomputed_parities = precompute_parities()
    # Get the table (should be in a driver function, not here)
    mask_size = 16
    bit_mask = 0xFFFF
    return (precomputed_parities[x>>(3*mask_size)] 
            ^ (precomputed_parities[x>>(2*mask_size)] & bit_mask) 
            ^ (precomputed_parities[x>>mask_size] & bit_mask) 
            ^ precomputed_parities[x] & bit_mask)
    # XOR ing each result automatically toggles and simplifies the result 
    # Use mask size to slide word to remove trailing bits
    # Use the bit mask to remove leading bits

def parity(x: int) -> bool:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    if(x):
        return True
    return False
    # XORing is commutative so we can get a log solution by 
    # XORing the last half with the first half of the words
