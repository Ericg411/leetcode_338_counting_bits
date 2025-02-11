from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(0, n + 1):
            binary_string = bin(i)
            counter = 0
            for c in binary_string:
                if c == '1':
                    counter += 1
            result.append(counter)
        return result