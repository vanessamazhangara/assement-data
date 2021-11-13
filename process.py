# log_file = open("um-server-01.txt") we open a file by using the "open" command and then pass in the string value of the file.


# def sales_reports(log_file): we've declared a function called sales_reports & passed in the log_file
#     for line in log_file:  (at this line we are looping through log_file)
#         line = line.rstrip() (rstrip removes the right end of each line we are looping)
#         day = line[0:3] (day is assigned to the first letters of the first index?)
#         if day == "Tue":
#             print(line)


# sales_reports(log_file)