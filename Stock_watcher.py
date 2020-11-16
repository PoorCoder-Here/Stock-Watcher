from selenium import webdriver
import csv
import sys
import datetime as dt
import time
path=#enter the path of webdriver
ntpc = webdriver.Chrome(path)
ntpc.get(#enter the url of the stock page)
time.sleep(5)
coalindia = webdriver.Chrome(path)
coalindia.get(#enter the url of the stock page)
time.sleep(5)
powergrid = webdriver.Chrome(path)
powergrid.get(#enter the url of the stock page)
time.sleep(5)
ioc = webdriver.Chrome(path)
ioc.get(#enter the url of the stock page)
time.sleep(5)
zeel = webdriver.Chrome(path)
zeel.get(#enter the url of the stock page)
time.sleep(5)
hindalco = webdriver.Chrome(path)
hindalco.get(#enter the url of the stock page)
time.sleep(5)
vedanta = webdriver.Chrome(path)
vedanta.get(#enter the url of the stock page)
time.sleep(5)
adanigas = webdriver.Chrome(path)
adanigas.get(#enter the url of the stock page)

now=dt.datetime.now()
d=now.strftime("%d-%m-%Y")
d1 = int(d[0:2])
m2 = int(d[3:5])
y1 = int(d[6:])
strt_time=now.strftime("%H:%M:%S")
print("Start_time:",strt_time)
strt_time=int(strt_time[0:2])
end=16
print("End_time:",str(end),':00:00')
f_name='Equity_NTPC_'+str(d)+'.csv'
f_bharat=open(f_name,'w',newline='')
wr_bharat=csv.writer(f_bharat,delimiter=',')
wr_bharat.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_COALINDIA_'+str(d)+'.csv'
f_nifty=open(f_name,'w',newline='')
wr_nifty=csv.writer(f_nifty,delimiter=',')
wr_nifty.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_POWERGRID_'+str(d)+'.csv'
f_reliance=open(f_name,'w',newline='')
wr_reliance=csv.writer(f_reliance,delimiter=',')
wr_reliance.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_IOC_'+str(d)+'.csv'
f_sbi=open(f_name,'w',newline='')
wr_sbi=csv.writer(f_sbi,delimiter=',')
wr_sbi.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_ZEEL_'+str(d)+'.csv'
f_tcs=open(f_name,'w',newline='')
wr_tcs=csv.writer(f_tcs,delimiter=',')
wr_tcs.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_HINDALCO_'+str(d)+'.csv'
f_tube=open(f_name,'w',newline='')
wr_tube=csv.writer(f_tube,delimiter=',')
wr_tube.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_VEDANTA_LTD_'+str(d)+'.csv'
f_vedanta=open(f_name,'w',newline='')
wr_vedanta=csv.writer(f_vedanta,delimiter=',')
wr_vedanta.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

f_name='Equity_ADANIGAS_'+str(d)+'.csv'
f_adanigas=open(f_name,'w',newline='')
wr_adanigas=csv.writer(f_adanigas,delimiter=',')
wr_adanigas.writerow(['DATE ','MONTH ','YEAR ','HOUR ','MINUTE ','SECOND ','PRICE '])

while strt_time<=end:
    print('\n')
    run = True
    while run:
        print("In run")
        try:
            bharat_price = ntpc.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = bharat_price.text
            bharat_pri = float(pri)
            print("NTPC_price:",bharat_pri)

            nifty_price = coalindia.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = nifty_price.text
            #pri1 = pri[:2] + pri[3:]
            nifty_pri = float(pri)
            print("COALINDIA:", nifty_pri)

            reliance_price = powergrid.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = reliance_price.text
            #pri1 = pri[:1] + pri[2:]
            reliance_pri = float(pri)
            print("POWERGRID_price:", reliance_pri)

            sbi_price = ioc.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = sbi_price.text
            sbi_pri = float(pri)
            print("IOC_price:", sbi_pri)

            tcs_price = zeel.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = tcs_price.text
            #pri1 = pri[:1] + pri[2:]
            tcs_pri = float(pri)
            print("ZEEL_price:", tcs_pri)

            tube_price = hindalco.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = tube_price.text
            tube_pri = float(pri)
            print("HINDALCO_price:", tube_pri)

            vedanta_price = vedanta.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = vedanta_price.text
            vedanta_pri = float(pri)
            print("VEDANTA_price:", vedanta_pri)

            adanigas_price = adanigas.find_element_by_xpath('//*[@id="knowledge-finance-wholepage__entity-summary"]/div/g-card-section/div/g-card-section/span[1]/span/span')
            pri = adanigas_price.text
            adanigas_pri = float(pri)
            print("ADANIGAS_price:", adanigas_pri)

            run = False
        except:
            ntpc.refresh()
            time.sleep(2)
            coalindia.refresh()
            time.sleep(2)
            powergrid.refresh()
            time.sleep(2)
            ioc.refresh()
            time.sleep(2)
            zeel.refresh()
            time.sleep(2)
            hindalco.refresh()
            time.sleep(2)
            vedanta.refresh()
            time.sleep(5)
            adanigas.refresh()

now = dt.datetime.now()
    time1 = now.strftime('%H:%M:%S')
    h1 = int(time1[0:2])
    m1 = int(time1[3:5])
    s1 = int(time1[6:])
    wr_bharat.writerow([d1, m2, y1, h1, m1, s1, bharat_pri])
    wr_nifty.writerow([d1, m2, y1, h1, m1, s1, nifty_pri])
    wr_reliance.writerow([d1, m2, y1, h1, m1, s1, reliance_pri])
    wr_sbi.writerow([d1, m2, y1, h1, m1, s1, sbi_pri])
    wr_tcs.writerow([d1, m2, y1, h1, m1, s1, tcs_pri])
    wr_tube.writerow([d1, m2, y1, h1, m1, s1, tube_pri])
    wr_vedanta.writerow([d1, m2, y1, h1, m1, s1, vedanta_pri])
    wr_adanigas.writerow([d1, m2, y1, h1, m1, s1, adanigas_pri])

    now = dt.datetime.now()
    time2 = now.strftime("%H:%M:%S")
    # print(time)
    m = int(time2[3:5])
    if m == 59:
        h = int(time2[0:2])
        if h <= 9:
            nh = '0' + str(h)
        nh = h + 1
        nm = '00'
        ns = '00'
    else:
        nh = int(time2[0:2])
        if nh <= 9:
            nh = '0' + str(nh)
        nm = m + 1
        if nm >= 1 and nm <= 9:
            nm = '0' + str(nm)
        ns = '00'
    n_time = str(nh) + ':' + str(nm) + ':' + str(ns)
    # print('next_time', n_time)
    while now != n_time:
        now = dt.datetime.now()
        now = now.strftime("%H:%M:%S")
        now1 = int(now[0:2])
        if now1 == end:
            #File closing
            f_bharat.close()
            f_nifty.close()
            f_reliance.close()
            f_sbi.close()
            f_tcs.close()
            f_tube.close()
            f_vedanta.close()
            f_adanigas.close()
            #Driver closing
            ntpc.close()
            coalindia.close()
            powergrid.close()
            ioc.close()
            zeel.close()
            hindalco.close()
            vedanta.close()
            adanigas.close()
            sys.exit()
    ntpc.refresh()
    coalindia.refresh()
    powergrid.refresh()
    ioc.refresh()
    zeel.refresh()
    hindalco.refresh()
    vedanta.refresh()
    adanigas.refresh()
    now = dt.datetime.now()
    strt_time = now.strftime('%H:%M:%S')
    print('\n')
    print(strt_time)
    strt_time = int(strt_time[0:2])
#File closing
f_bharat.close()
f_nifty.close()
f_reliance.close()
f_sbi.close()
f_tcs.close()
f_tube.close()
f_vedanta.close()
f_adanigas.close()
#Driver closing
ntpc.close()
coalindia.close()
powergrid.close()
ioc.close()
zeel.close()
hindalco.close()
vedanta.close()
adanigas.close()