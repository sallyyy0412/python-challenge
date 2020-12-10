import csv

csvpath = "C:/python-challenge/bypoll/resources/02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv"

with open(csvpath, newline='') as csvfile:
	# 讀取 CSV 檔案內容
	rows = csv.reader(csvfile)
	# 總投票數
	totalVotes = 0
	# 候選人清單
	candidates = []
	# 得票清單
	numberOfVotes = []
	# 跳過標題row
	skipFirstRow = False
	for row in rows:
		# 還沒跳過標題row
		if not skipFirstRow:
			# 那就跳過
			skipFirstRow = True
			# 下面一位~
			continue
		# 提取候選人名稱
		candidateName = row[2]
		# 總投票數+1
		totalVotes += 1
		# 若該候選人有在清單內
		if candidateName in candidates:
			# 取得索引
			candidateIndex = candidates.index(candidateName) 
			# 該索引得票數+1
			numberOfVotes[candidateIndex] += 1
		else:
			# 加入至候選人清單
			candidates.append(candidateName)
			# 計1票
			numberOfVotes.append(1)



	# 結果輸出
	print('Election Results')
	print('-------------------------')
	print('Total Votes:', totalVotes)
	print('-------------------------')
	# 把每位候選人列出
	for i in range(0, len(candidates)):
		print(candidates[i] + ':', str('%.3f'%(numberOfVotes[i]/totalVotes * 100)) + '%', '(' + str(numberOfVotes[i]) + ')')
	print('-------------------------')
	# 取得最高票數索引
	maxVoteIndex = numberOfVotes.index(max(numberOfVotes))
	print('Winner:', candidates[maxVoteIndex])
	print('-------------------------')


output = "C:/python-challenge/bypoll/analysis/output.txt"

with open(output, 'w') as file:
	file.write('Election Results')
	file.write('\n')
	file.write('----------------------------')
	file.write('\n')
	file.write('Total Votes:'+ str(totalVotes))
	file.write('\n')
	file.write('----------------------------')
	file.write('\n')
	
	
	
	for i in range(0, len(candidates)):
		file.write(candidates[i] + ":" + str('%.3f'%(numberOfVotes[i]/totalVotes * 100)) + '%' + '(' + str(numberOfVotes[i]) + ')')
		file.write('\n')
		maxVoteIndex = numberOfVotes.index(max(numberOfVotes))
		file.write('\n')
		
	file.write('----------------------------')
	file.write('\n')
	file.write('Winner:' + candidates[maxVoteIndex])
	file.write('\n')
	file.write('----------------------------')
            
            
            
            
            
