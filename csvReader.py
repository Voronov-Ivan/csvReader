import csv
new_rows = []
workers = []
all_date = []
workers_hours = []
final_row = []
with open("acme_worksheet.csv", newline = "") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        if(row["Employee Name"] not in workers):
            workers.append(row["Employee Name"])
        if(row["Date"] not in all_date):
            all_date.append(row["Date"])
        dict = {"name":row["Employee Name"],"Date":row["Date"],"Work Hours":row["Work Hours"]}
        new_rows.append(dict)
for worker in workers:
    workers_hours.append({"name":worker})
    for person in workers_hours:
        for date in all_date:
            person[date] = "0"
        for dict in new_rows:
            if(person["name"] == dict["name"]):
                person[dict["Date"]] = dict["Work Hours"]
for person in workers_hours:
    final_row.append(person.values())
with open("new_acme_worksheet.csv","w", newline = "") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    first_row = ["Name/Date"]+all_date
    writer.writerow(first_row)
    for person in final_row:
        writer.writerow(person)
