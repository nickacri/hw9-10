def calc(radius, height):
    areaTop = (3.14 * radius**2)
    areaSides = radius * height * 3.14**2
    areaTotal = areaTop + areaSides
    sqFeet = areaTotal / 144
    mCost = 25 * sqFeet
    lCost = 15 * sqFeet
    totalCost = mCost + lCost
    print(totalCost)
    return totalCost

def main():
    radius = int(input("What is your radius?"))
    height = int(input("What is your height?"))
    estimateCost = calc(radius, height)

    print(estimateCost)


    main()
