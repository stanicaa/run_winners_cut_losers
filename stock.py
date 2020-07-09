"""
single stock testing. The input here is a variable bb, which is a pandas variable holding the stock prices, while stock is the "header"
of the column for the stock that is being analyzed.
"""

def single(bb, stock):
    s=bb[stock]
    b=0
    profit=0
    for i in range(len(s)-2):
        #position initiation condition
        if s.iloc[i+2]>s.iloc[i]:
            if i>20:
                if s.iloc[i+2]>s.iloc[i-5]:
                    if b==0:
                        b=s.iloc[i+2] #initiating a position
                        counting=0
        #loss cut discipline
        if b>0:
            if s.iloc[i+2]<0.97*b:
                pp=s.iloc[i+2]-b #cutting losses
                profit+=pp
                b=0 #re-setting the value of our position after selling it
                counting=i+2
        #position closing condition
        if s.iloc[i+2]<s.iloc[i]:
            if b>0:
                ps=s.iloc[i+2]-b
                profit+=ps
                #print('SELLING: ', b, s.index[i+2], s[i+2], profit)
                b=0
                counting=i+2
    #liquidating position at the end
    if b>0:
        final=s.iloc[-1]-b
    else:
        final=0
    final_profit=profit+final
    return final_profit
