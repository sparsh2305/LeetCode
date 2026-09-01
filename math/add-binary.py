class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r_bin = bin(int(a,2) + int(b,2))[2:]

        rfmt = f"{int(a, 2) + int(b, 2):b}"

        return(r_bin)  
        return(rfmt)
        