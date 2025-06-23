import copy
count = 0
class Solution:
    def countArrangement(self, n: int) -> int:
        """
        TC: O(n!)
        AS: O(n)
        """

        arr = [i for i in range(1, n + 1)]
        result = []
        path = []
        self.count = 0

        def helper(idx, nums):

            # base condition
            if idx > n:
                self.count += 1
                return

            # logic
            for i in range(len(nums)):
                num = nums[i]

                if num % idx == 0 or idx % num == 0:
                    # action: choose num, remove from candidates
                    path.append(num)
                    next_nums = nums[:i] + nums[i+1:]
                    
                    # recurse to next position
                    helper(idx + 1, next_nums)

                    # backtrack
                    path.pop()

        helper(1, arr)
        return self.count
    



if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.countArrangement(n))
