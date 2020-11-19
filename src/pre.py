import json
import csv
import time

names =['Niklas Henschel', 'Janne Savikko', 'Tuomas Hietala', 'Julia Shamrina', 'Jaakko Malkamäki', 'Leena Romppainen']

with open('hehe.csv', 'w', encoding='UTF-8') as wf:
    writer = csv.writer(wf, delimiter=',', lineterminator='\n')
    head = ['index', 'id', 'status', 'subject', 'requester', 'req_site', 'assignee', 'ass_site']
    for i in range(29):
        head.append(i+1)
    head.append('commment_sum')
    writer.writerow(head)

    with open('ticket1.json', 'r', encoding='UTF-8') as rf:
        j = 0
        for i, row in enumerate(rf):
            if (i > -1):
                tobe = False
                a = json.loads(row)
                if (a['assignee'] and a['assignee']['name'] in names and '2020-02' in a['created_at']):
                    if (a['comments']):
                        #print(a['created_at'])
                        number = 0
                        row_arr = [i, a['id'], a['status'], a['subject'], a['requester']['name'], a['requester']['time_zone'], a['assignee']['name'], a['assignee']['time_zone']]
                        for index in range(29):
                            row_arr.append(0)
                        for comment in a['comments']:
                            if ('2020-02' in comment['created_at']):
                                tobe = True
                                timeArray = time.strptime(comment['created_at'], "%Y-%m-%dT%H:%M:%S.000Z")
                                date_d = int(time.strftime("%d", timeArray))
                                #print(comment['created_at'])
                                if (0 < date_d and date_d < 30):
                                    row_arr[date_d+7] = row_arr[date_d+7] + 1
                        sum = 0
                        for i in range(8, len(row_arr)-1):
                            sum += row_arr[i]
                        #print(sum)
                        row_arr.append(sum)
                        writer.writerow(row_arr)
                    else:
                        print("hh")
                if (tobe == True):
                    j = j + 1
                    print(j)