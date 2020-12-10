import csv

csvpath = "C:/python-challenge/bybank/resources/02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv"

    
with open(csvpath, newline='') as csvfile:
	# 讀取 CSV 檔案內容
	rows = csv.reader(csvfile)
	# 總盈虧
	total = 0
	# 總月數 
	monthCount = 0
	# 上月盈虧 
	lastAccount = 0
	# 總增減 
	totalChange = 0
	# 盈利最多月份, 預設為無 
	greatestIncrease = ['', 0]
	# 虧損最多月份, 預設為無 
	greatestDecrease = ['', 0]
	# 跳過標題row  
	skipFirstRow = False
	
	for row in rows:
		# 還沒跳過標題row  
		if not skipFirstRow:
			# 那就跳過
			skipFirstRow = True
			# 下面一位~
			continue
		
		# 本月名稱 
		currentMonth = row[0]
		# 本月盈虧
		currentAccount = int(row[1])
		# 加總本月盈虧
		total += currentAccount
		
		# 排除第一個月，每個月的增減之加總
		if lastAccount == 0:
			# 月增減(與上月比較)
			monthChange = (currentAccount - lastAccount)
			# 總增減
			totalChange += monthChange
			# 若月增減超過目前最高記錄
			if monthChange > greatestIncrease[1]:
				# 則列為新最高記錄
				greatestIncrease = [currentMonth, monthChange]
			# 若月增低於過目前最低記錄
			if monthChange < greatestDecrease[1]:
				# 則列為新最低記錄
				greatestDecrease = [currentMonth, monthChange]
		# 月計數+1
		monthCount += 1
		# 列為上個月盈虧
		lastAccount = currentAccount
	

	print('Financial Analysis')
	print('----------------------------')
	print('Total Months:', monthCount)
	print('Total: ', '$' + str(total))
	print('Average  Change:', '$' + str(round(totalChange / (monthCount - 1), 2)))
	print('Greatest Increase in Profits:', greatestIncrease[0], '($' + str(greatestIncrease[1]) + ')')
	print('Greatest Decrease in Profits:', greatestDecrease[0], '($' + str(greatestDecrease[1]) + ')')

output = "C:/python-challenge/bybank/analysis/output.txt"

with open(output, 'w') as file:

	
	
	file.write('Financial Analysis')
	file.write('\n')
	file.write('----------------------------')
	file.write('\n')
	file.write('Total Months: ' + str(monthCount))
	file.write('\n')
	file.write('Total: $' + str(total))
	file.write('\n')
	file.write('Average  Change: $' + str(round(totalChange / (monthCount - 1), 2)))
	file.write('\n')
	file.write('Greatest Increase in Profits:' + greatestIncrease[0] + '($' + str(greatestIncrease[1]) + ')')
	file.write('\n')
	file.write('Greatest Decrease in Profits:' + greatestDecrease[0] + '($' + str(greatestDecrease[1]) + ')')
	
  
