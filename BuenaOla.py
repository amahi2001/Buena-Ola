import pandas as pd  # for data analytics

import matplotlib.pyplot as plt  # for plotting

import yfinance as yf  # for financial data access

import numpy as np  # for array/ matrix manipulations

from IPython.display import display  # for ease of testing

from sklearn.linear_model import LinearRegression  # for linear regresion

def analyze(ticker):
    # GPRE
    if(ticker == "1"):

        # creating a data frame to access sutainability data
        gpre = pd.read_excel('data.xlsx', sheet_name='GPRE')

        # creating a dataframe of earnings data
        tick = yf.Ticker("GPRE")
        earnings = tick.earnings

        result = pd.merge(gpre, earnings, how='inner', on='Year')

        # display(result)
        inp = input(
            '\nWhich data comparison would you like to use ?: \n(1) Total GHG emissions(Thousand Metric Tons)\n(2) Electricity Use (Thousand Megawatt Hours)\n(3)Total Water Use (thousand cubic meters)\n(4) Compare all\n')

        # come back to this to implement labels and legends
        if(inp == '1'):
            # result['E/S'] = result['Earnings'] / result["Total GHG emissions (Thousand Metric Tons)"]
            # plt.plot(result["Year"], result['Earnings'])

            regDF = pd.DataFrame()
            regDF['X'] = result['Total GHG emissions (Thousand Metric Tons)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')
            plt.show()

        elif(inp == '2'):
            regDF = pd.DataFrame()  # creating an empty dataframe
            regDF['X'] = result['Electricity Use (Thousand Megawatt Hours)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')
            plt.show()

        elif(inp == '3'):
            regDF = pd.DataFrame()  # creating an empty dataframe
            regDF['X'] = result['Total Water Use (thousand cubic meters)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')
            plt.show()

        elif(inp == '4'):

            # GHG Emissions
            regDF = pd.DataFrame()
            regDF['A'] = result['Total GHG emissions (Thousand Metric Tons)']
            regDF['B'] = result['Earnings']

            X1 = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y1 = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X1, Y1)  # perform linear regression
            earnPredict = linear_regressor.predict(X1)  # make predictions

            plt.scatter(X1, Y1)
            plt.plot(X1, earnPredict, color='blue')

            # Electricity used
            regDF1 = pd.DataFrame()  # creating an empty dataframe
            regDF1['C'] = result['Electricity Use (Thousand Megawatt Hours)']
            regDF1['D'] = result['Earnings']

            X2 = regDF1.iloc[:, 0].values.reshape(-1, 1)
            Y2 = regDF1.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X2, Y2)  # perform linear regression
            earnPredict = linear_regressor.predict(X2)  # make predictions

            plt.scatter(X2, Y2)
            plt.plot(X2, earnPredict, color='orange')

            # Total Water use
            regDF = pd.DataFrame()  # creating an empty dataframe
            regDF['E'] = result['Total Water Use (thousand cubic meters)']
            regDF['F'] = result['Earnings']

            X3 = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y3 = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X3, Y3)  # perform linear regression
            earnPredict = linear_regressor.predict(X3)  # make predictions

            plt.scatter(X3, Y3)
            plt.plot(X3, earnPredict, color='green')

            plt.show()

        else:
            print("\n**error, invalid input, pleae enter valid input**\n")
            analyze("1")

        restart()

    # RUN
    elif(ticker == "2"):
        run = pd.read_excel('data.xlsx', sheet_name='RUN')

        tick = yf.Ticker("RUN")
        earnings = tick.earnings

        result = pd.merge(run, earnings, how='inner', on='Year')
        # display(result)
        inp = input(
            '\nWhich data comparison would you like to use ?: \n(1)Total Emissions (Thousand MT CO2) \n(2) Nitrogen Oxide (MT Prevented)\n(3) Ozone (MT Prevented)\n(4) Compare all\n')

        if(inp == '1'):
            # plt.scatter(
            #     result["Total Emissions (Thousand MT CO2)"],
            #     result['Earnings'])
            regDF = pd.DataFrame()
            regDF['X'] = result['Total Emissions (Thousand MT CO2)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')

            plt.show()

        elif(inp == '2'):
            # plt.scatter(
            #     result['Nitrogen Oxide (MT Prevented)'],
            #     result['Earnings'])
            regDF = pd.DataFrame()
            regDF['X'] = result['Nitrogen Oxide (MT Prevented)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')

            plt.show()

        elif(inp == '3'):
            # plt.scatter(
            #     result['Ozone (MT Prevented)'],
            #     result['Earnings'])
            regDF = pd.DataFrame()
            regDF['X'] = result['Ozone (MT Prevented)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')
            plt.show()

        elif(inp == '4'):
            regDF = pd.DataFrame()
            regDF['X'] = result['Total Emissions (Thousand MT CO2)']
            regDF['Y'] = result['Earnings']

            X = regDF.iloc[:, 0].values.reshape(-1, 1)
            Y = regDF.iloc[:, 1].values.reshape(-1, 1)
            linear_regressor = LinearRegression()  # create object for the class
            linear_regressor.fit(X, Y)  # perform linear regression
            earnPredict = linear_regressor.predict(X)  # make predictions

            plt.scatter(X, Y)
            plt.plot(X, earnPredict, color='red')

            plt.show()
        # error-handling for invalid input
        else:
            print("\n**error, invalid input, pleae enter valid input**\n")
            analyze("2")
        restart()


# allows user to restart or end the program, also allows for ease of testing
def restart():
    answer = input(
        "would you like to restart the program? :\n(1)YES, (2)NO\n\n")

    if(answer == '1'):
        main()
    elif(answer == '2'):
        print('Have a good day!\n')
    else:
        print("please input a valid answer (1 or 2)\n")
        restart()


# main function: deals with user interface
def main():
    ticker = input(
        "\nWhich company would you like to analyze? \n(1)GPRE \n(2)RUN \n\nPlease enter 1 or 2: \n")
    if(ticker == "1"):
        print("GPRE\n")
        analyze(ticker)
    elif(ticker == "2"):
        print("RUN\n")
        analyze(ticker)
        print("\n**invalid entry**, please enter 1 or 2 into the console\n")
        main()


if __name__ == "__main__":
    # redirecting main function for easier recursion
    main()
