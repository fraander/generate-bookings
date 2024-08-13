import pandas as pd

df = pd.read_csv('data.csv')
df = df.drop('Timestamp', axis=1)
df = df.drop('Northeastern Email', axis=1)

times = [ "5:30pm to 5:45pm", "5:45pm to 6:00pm", "6:00pm to 6:15pm", "6:15pm to 6:30pm", "6:30pm to 6:45pm", "6:45pm to 7:00pm", "7:00pm to 7:15pm", "7:15pm to 7:30pm", "7:30pm to 7:45pm", "7:45pm to 8:00pm", "8:00pm to 8:15pm", "8:15pm to 8:30pm", "8:30pm to 8:45pm", "8:45pm to 9:00pm", "9:00pm to 9:15pm", "9:15pm to 9:30pm", "9:30pm to 9:45pm", "9:45pm to 10:00pm"]

# print(cols)



values = []
for index, row in df.iterrows():
    for timeIndex in range(0, len(times)):
        days = row[timeIndex + 3]
        for day in days.split(', '):
            out = [row[0], row[1], row[2], day, times[timeIndex]]
            values.append(out)

of = pd.DataFrame(values, columns=['Email', 'Team', 'Size', 'Day', 'Time'])
print(of.to_string())
of.to_csv("output.csv", index=False)


# print("df")
# print(df.to_string())