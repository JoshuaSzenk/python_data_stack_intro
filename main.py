import profile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])

#print(s)

dates = pd.date_range("20260512", periods=6)
#print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
#print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20260512"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
#print(df2)
#print(df2.dtypes)

#print(df.head(2))
#print(df.tail(3))

#print(df.index)
#print(df.columns)

#print(df.to_numpy())
#print(df2.to_numpy())

#print(df.describe())

#print(df.T)

#print(df.sort_index(axis=1, ascending=False))

#print(df.sort_values(by="B"))

#print(df["A"])
#print(df.A)

#print(df[["B", "A"]])

#print(df[0:3])
#print(df["20260513":"20260515"])

#print(df.loc[dates[0]])
#print(df.loc[:, ["A", "D"]])
#print(df.loc["20260513":"20260515", ["A", "B"]])

#print(df.loc[dates[0], "A"])
#print(df.at[dates[0], "A"])

#print(df.iloc[3])
#print(df.iloc[3:5, 0:2])
#print(df.iloc[[1, 2, 4], [0, 2]])
#print(df.iloc[1:3, :])
#print(df.iloc[1, 1])
#print(df.iat[1, 1])

#print(df[df > 0])
#print(df[df < 0])

df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
#print(df2)
#print(df2[df2["E"].isin(["two", "one"])])

s1 = pd.Series(
    [1,2,3,4,5,6],
    index=pd.date_range("20260512", periods=6))

#print(s1)

df["F"] = s1
#print(df)

df.at[dates[0], "A"] = 0
df.iat[0, 1] = 0
df.loc[:, "D"] = np.array([5] * len(df))
#print(df)

df2 = df.copy() #erstellt eine copy von df in df2
df2[df2 > 0] = -df2 #überschreibt alle positive von df2 mit ihren negativen
#print(df2)

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"]) #ich verkleiner die Tabelle auf 4 Tage und mache eine neue spalte E
df1.loc[dates[0] : dates[1], "E"] = 1 #in die ersten 2 Zeilen der Spalte E wird 1.0 eingetragen
#print(df1)
df1.at[dates[0], "F"] = np.nan #in Zeile 1 und Spalte F ein NaN erzeugen
#print(df1)

#print(df1.dropna(how="any"))

#print(df1.fillna(value=5))

#print(pd.isna(df1))

#print(df.mean())
#print(df.mean(axis=1))

s = pd.Series([1,3,5, np.nan, 6, 8], index=dates).shift(2) #erstelle neue Liste s, Shift(2) schiebt die werte um 2 nach unten daher ersten beie NaN
#print(s)
#print(df.sub(s, axis="index"))

#print(df.agg(lambda x: np.mean(x) * 5.6))
df["F"] = df["F"].shift(1)
resultat = df.transform(lambda x: x * 101.2)
#print(resultat)

s = pd.Series(np.random.randint(0, 7, size=10)) #es werden 10 Zahlen random ausgespuckt in der range von 0-7
#print(s)
#print(s.value_counts())

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
#print(s.str.lower())

df = pd.DataFrame(np.random.randn(10,4)) #neues df mit 10 Zeilen und random zahlen in 4 Spalten
#print(df)
pieces = [df[:3], df[3:7], df[7:]] #zerleg das DataFrame in 3 verschiedene Teile
#print(pd.concat(pieces))

#left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
#right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
#print(left)
#print(right)
#print(pd.merge(left, right, on="key"))

left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
#print(pd.merge(left, right, on="key"))

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
#print(df)
#print(df.groupby("A")[["C", "D"]].sum())
#print(df.groupby(["A", "B"]).sum())

arrays = [
   ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
   ["one", "two", "one", "two", "one", "two", "one", "two"],
] #es werden zwei Listen erstellt

index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"]) #hier werden die listen kombiniert
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"]) # es werdn zufalsswerte erstellt für spalte A und B
df2 = df[:4] # werden nur die ersten 4 in df2 gespeichert

#print(df2)

stacked = df2.stack()
#print(stacked)

#print(stacked.unstack())
#print(stacked.unstack(0))
#print(stacked.unstack(2))

df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
) # neues DataFrame erstellen

#print(df)

#print(pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"]))

rng = pd.date_range("1/1/2012", periods=100, freq="s") #hier wird eine liste von zeitstempel generiert, 100 stück in einem sekündlichen abstand, also 100 stempel in 1 minute 40 sekunden
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng) #erstelle eine serie mit zufallszahlen zwischen 0 und 500 und jede bekommt einen zeitstempel als index

#print(ts.resample("5Min").sum())

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D") #es wird ein Datumsbereich für 5 aufeinanderfolgende Tage erstellt beginnend am 06.03.2012
ts = pd.Series(np.random.randn(len(rng)), rng) #die Zeitstempel werden als Index für eine Reihe von Zufallszahlen genutzt

#print(ts)

ts_utc = ts.tz_localize("UTC") #Diese Daten stammen aus der Weltzeit UTC

#print(ts_utc)

#print(ts_utc.tz_convert("US/Eastern"))
#print(ts_utc.tz_convert("EUROPE/BERLIN"))

#print(rng)
#print(rng + pd.offsets.BusinessDay(5))

df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
) #neues DataFrame

df["grade"] = df["raw_grade"].astype("category") #ich mache aus raw_grades eine Categorie
#print(df["grade"])

new_categories = ["very good", "good", "very bad"] #ich erstelle eine neue Kategroie
df["grade"] = df["grade"].cat.rename_categories(new_categories) #ich ersetze die alte kategorie durch die neue

df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"] #hier macg ich die reienfolge 
)

#print(df["grade"])
#print(df.sort_values(by="grade"))
#print(df.groupby("grade", observed=False).size())

plt.close("all")

ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()

#(ts.plot())
#plt.show()

df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
) # Erstelle eine Tabelle mit 1000 Zeilen und 4 Spalten mit Zufallszahlen

df = df.cumsum() #kummuliert die summe der kategorien
df.plot() #teilt sie in verschiedene farben
plt.legend(loc='best') #erstellt legende
plt.show() #plotet das diagramm, quasi wie print

df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
#df.to_csv("foo.csv") #im projektordner wird eine CSV namens foo.csv erstellt

#print(pd.read_csv("foo.csv"))

df.to_excel("foo.xlsx", sheet_name="Sheet1") #im projektordner wird gier eine Excel erstellt namens foo.xlsx

#print(pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"]))

#if pd.Series([False, True, False]).any(): #Löst aus wenn mindestens ein Wert in der Liste wahr ist
     #print("I was true")

