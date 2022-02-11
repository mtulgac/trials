def costCalculator(value, index, matriceList):
    if len(matriceList) == 2:
        m1 = matriceList[0]
        m2 = matriceList[1]
        costList2 = [] 
        for b in range(m1.shape[1]):
            costList = []
            for i in range(m2.shape[1]):
                calculatedCost = value + m1[index][b] + m2[b][i]
                costList.append(calculatedCost)
            costList2.append(costList)
        return costList2
    else:
        currentMatrice = matriceList[0]
        costList2 = []
        for i in range(currentMatrice.shape[0]):
            for j in range(currentMatrice.shape[1]):
                currentMatriceValue = currentMatrice[i][j] + value
                costList2.append(costCalculator(currentMatriceValue, j, matriceList[1:]))
        return costList2