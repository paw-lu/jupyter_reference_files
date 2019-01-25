# This makes a df pretty and can even output a pdf

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import pandas as pd
import numpy as np
import six

# Dictionary to traslate from acronyms to full product name used in database
product_names = {
    'SLR': ['Student Loan Refinance', 'Eagle All In One'],
    'PLP': ['Eagle Partner Loans'],
    'One for business': ['Eagle One'],
    'Gold': ['Eagle Gold'],
    'HELOC': [
        'HELOC - Repayment Period',
        'Home Equity Line Of Credit',
        'Home Equity Line Of Credit - No Closing Costs',
        'HOME EQUITY LINE OF CREDIT'
         ]
}

eagle_loans = ('SLR', 'PLP', 'One', 'Gold', 'HELOC')
summary_stats = (
    'Total loans originated since inception',
    'Outstanding loans',
    'Household with outstanding eagle loan',
    'Households who still bank at FRB',
    '% New to FRB',
    'Outstanding commitment balance',
    'Median commitment balance per HH',
    'Outstanding current balance',
    'Median current balance per HH',
    'Deposit',
    'Median deposit',
    '% Funded (deposit to outstanding balance)',
    'Average AUM',
    'Households with an SFR loan post Eagle Loan',
    '% Active client',
    'Median age at origination',
    'Weighted avg rate',
    'Median FICO',
    'YTD gross charge-offs'
)

test_df = pd.DataFrame(np.random.randn(19,6), columns=list(product_names.keys())+['Totals'], index=summary_stats)
df = test_df.copy().round(decimals=4)

def print_df(data, col_width=5.0, row_height=2.0, font_size=30,
                     header_color='#ffffff', row_colors=['#ffffff'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=[-1], header_rows=[-1],
                     bold_columns=[-1], bold_rows=[-1],
                     ax=None, export=False, title=None, **kwargs):

    plt.rcParams['font.sans-serif'] = 'Roboto'
    font_color = (0,0,0,0.87)
    plt.rcParams['text.color'] = font_color
    plt.rcParams['axes.labelcolor'] = font_color
    plt.rcParams['xtick.color'] = font_color
    plt.rcParams['ytick.color'] = font_color

    new_column_order = [' '] + df.columns.tolist()
    data[' '] = data.index
    data = data[new_column_order]

    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width+1.0, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    colWidths = [2.95] + [1.0 for _ in range(data.shape[1]-1)]
    ax.axis([data.shape[1],-1,data.shape[0],-1])
    mpl_table = ax.table(cellText=data.values,
                         bbox=bbox, colLabels=data.columns, colLoc='left', cellLoc='right',
                         rowLoc='left', colWidths=colWidths, **kwargs) #rowLabels=data.index.values,

    index_cells = [key for key in mpl_table._cells if key[1] == 0]
    for cell in index_cells:
        mpl_table._cells[cell]._loc = 'left'

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    #ax.axvline(0, color=(0,0,0,0.1), linewidth=2)
    ax.axvline(4.4, color=(0,0,0,0.1), linewidth=2)
    for row in range(data.shape[0]):
        ax.axhline(row, color=(0,0,0,0.1), linewidth=2)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] in bold_rows or k[1] in bold_columns:
            cell.set_text_props(color=(0,0,0,0.87), weight='bold')

        if k[0] in header_rows or k[1] in header_columns:
            cell.set_facecolor(header_color)
            cell.set_text_props(color=(0,0,0,0.60))
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])

    if title:
        ax.set_title(title, fontsize=60, loc='left', x=0.035, y=1.02)


    if export:
        fig.savefig("test.pdf") # add bbox_inches='tight' to fill page

    return ax

print_df(df, bold_columns=[6], header_rows=[0], export=True, title="Eagle summary by product");
