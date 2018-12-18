import pygal
def chart(year, number):
    buy, sell = [], []
    for i in year:
        i = i.split()
        buy.append(float(i[1]))
        sell.append(float(i[2]))
    line = pygal.Line()
    line.title = "Buy and Sell in "+number
    line.x_labels = map(str, range(1, 12))
    line.add('Buy', buy[12::-1])
    line.add('Sell', sell[12::-1])
    line.render_to_file("../img/"+number+'.svg')
def main():
    chart(open("../data/data17.txt", "r"), "2017")
    chart(open("../data/data1.txt", "r"), "2001")
    chart(open("../data/data0.txt", "r"), "2000")
main()
