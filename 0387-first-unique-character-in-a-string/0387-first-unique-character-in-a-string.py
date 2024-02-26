class Solution:
    def firstUniqChar(self, s: str) -> int:
        positions = {}
        for idx,ch in enumerate(s):
            if ch not in positions:
                positions[ch] = [idx]
            else:
                positions[ch].append(idx)
        minNonRepeatingIdx = float('inf')
        for k,v in positions.items():
            if len(v) == 1:
                minNonRepeatingIdx = min(minNonRepeatingIdx,v[0])
        return -1 if minNonRepeatingIdx == float('inf') else minNonRepeatingIdx