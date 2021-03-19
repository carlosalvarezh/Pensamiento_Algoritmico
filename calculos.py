def calculos(ladoa, ladob, ladoc):
    s = (ladoa + ladob + ladoc) / 2
    Area = (s*(s-ladoa)*(s-ladob)*(s-ladoc))**0.5
    return s, Area