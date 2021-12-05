from flask import Flask,render_template
import sqlite3    #数据库
import jieba  #分词
from matplotlib import pyplot as plt  #绘图，数据可视化
from wordcloud import wordcloud  #词云
from PIL import Image       #图片处理
import numpy as np       #矩阵运算


app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')
@app.route('/index')
def home():  # put application's code here
    # return render_template('index.html')
    return  index()
@app.route('/movie')

def movie():  # put application's code here
    datalist = []
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('movie.html',movies = datalist)
@app.route('/score')
def score():  # put application's code here
    score =[]  #评分
    number = [] #每个评分统计的电影数量
    conn = sqlite3.connect('movie.db')
    cur = conn.cursor()
    sql = 'select score,count(score) from movie250 group by score'
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        number.append(item[1])
    cur.close()
    conn.close()
    return render_template('score.html',score=score,number=number)

@app.route('/word')
def word():  # put application's code here
    # conn = sqlite3.connect('movie.db')
    # cur = conn.cursor()
    # sql = 'select instroduction from movie250'
    # data = cur.execute(sql)
    # text = ""
    # for item in data:
    #     text = text + item[0]
    #     # print(item[0])
    # cur.close()
    # conn.close()
    # cut = jieba.cut(text)
    # string = ' '.join(cut)
    #
    # img = Image.open(r'./static/assets/img/tree.jpeg') #打开遮罩图片
    # img_array = np.array(img)  #将图片转换为数组
    # print(img_array)
    # wc = wordcloud(
    #     background_color='white',
    #     mask=img_array,
    #     font_path='msyh.ttc')
    # wc.generate_from_text(string)
    #绘制图片
    # fig = plt.figure(1)
    # plt.imshow(wc)
    # plt.axis('off') #是否显示坐标轴
    # plt.show()
    return render_template('word.html')
@app.route('/team')
def team():  # put application's code here
    return render_template('team.html')

if __name__ == '__main__':
    app.run()

