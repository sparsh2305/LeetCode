class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1

        for i in range(2, num // 2 + 1):
            if num % i == 0:
                total += i

        return total == num