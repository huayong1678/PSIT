"""Annual Information 2000 to 2017"""
import csv
def table(year, number):
    file = open("Table_ForeignTrade.csv", "r", encoding="utf-8") #Open main data
    data = csv.reader(file)
    table = [row for row in data]
    for i in table:
        if number in i[0]:
            year.write(i[0]+" "+i[1]+" "+i[2]+"\n")
    year.close() #Always close files after use
def main():
    table(open("data17.txt", "w"), "2017")#Open file for writing
    table(open("data16.txt", "w"), "2016")
    table(open("data15.txt", "w"), "2015")
    table(open("data14.txt", "w"), "2014")
    table(open("data13.txt", "w"), "2013")
    table(open("data12.txt", "w"), "2012")
    table(open("data11.txt", "w"), "2011")
    table(open("data10.txt", "w"), "2010")
    table(open("data9.txt", "w"), "2009")
    table(open("data8.txt", "w"), "2008")
    table(open("data7.txt", "w"), "2007")
    table(open("data6.txt", "w"), "2006")
    table(open("data5.txt", "w"), "2005")
    table(open("data4.txt", "w"), "2004")
    table(open("data3.txt", "w"), "2003")
    table(open("data2.txt", "w"), "2002")
    table(open("data1.txt", "w"), "2001")
    table(open("data0.txt", "w"), "2000")
main()
