class Solution:
    def check(self,positions,mid):
        curr=positions[0]
        ans=1
        for i in range(1,len(positions)):
            if positions[i]-curr>=mid:
                ans+=1
                curr=positions[i]
        return ans
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n=len(position)
        l=0
        r=position[-1]-position[0]
        while l<r:
            mid=r-(r-l)//2
            if self.check(position,mid)>=m:
                l=mid
            else:
                r=mid-1
            #print(l,r)    
        return l
                
        