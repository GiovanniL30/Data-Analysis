# Author: Kevin Roy Maglaqui
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('job_posting_clean.csv')

#list all the number of applications
#df.applies.to_string(index=False)

most_applications = df.loc[df['applies'].idxmax()]

print("Job posting that have the most applications")
print(most_applications)

# Graph of the most applied jobs
top_jobs = df.nlargest(10, 'applies')
plt.figure(figsize=(12,6))
sns.barplot(x='applies', y ='title', data=top_jobs, palette='viridis')
plt.title("Most applied Jobs (July 2023-November 2023)")
plt.xlabel("Applications")
plt.ylabel("Job Title")
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()