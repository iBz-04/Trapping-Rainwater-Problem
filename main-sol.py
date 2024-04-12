class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        def get_prefix_max(h):
            prefix = [0]
            for i in range(N):
                prefix.append(max(h[i], prefix[-1]))
            return prefix
        
        left = get_prefix_max(height)
        right = get_prefix_max(height[::-1])[::-1]
        
        water = 0
        for i in range(N):
            water += max(min(left[i], right[i + 1]) - height[i], 0)
            
        return water
