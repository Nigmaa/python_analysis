import pandas as pd

def lesson8():
    df = pd.read_csv('上市公司資料.csv')
    df1 = df.dropna()
    df2 = df1.reindex(columns=['公司代號','出表日期','公司名稱','產業別','營業收入-當月營收','營業收入-上月營收'])
    df3 = df2.to_csv('上市公司資料_清理.csv', encoding='utf-8')
    df4 = df2.to_excel('上市公司資料_清理.xlsx')
    print('檔案已存檔完成')

if __name__ == '__main__':
    lesson8()
