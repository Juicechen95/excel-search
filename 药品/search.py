# coding: utf8
import xlrd



def getdat(name):
        fname = "data.xlsx"
        bk = xlrd.open_workbook(fname)
        shxrange = range(bk.nsheets)
        try:
                sh = bk.sheet_by_name("Sheet1")
        except:
        	print ("no sheet in %s named Sheet1" % fname)
        #获取行数
        nrows = sh.nrows
        #获取列数
        ncols = sh.ncols
        #print ("nrows %d, ncols %d" % (nrows,ncols))
        #获取第一行第一列数据
        cell_value = []
        cell_value.append(sh.cell(0,0).value)
        #print (cell_value)
        data=[]
        datlog={}
        #获取各行数据
        for i in range(nrows):
                data_row=[]
                for j in range(ncols):
                        data_row.append(sh.cell(i,j).value)
                data.append(data_row)
        for i in range(nrows):
                datlog[data[i][0]]=data[i]
        print (datlog[name])


if __name__ == '__main__':
        name=input('请输入查询的化学剂名称：')
        getdat(name)
        
