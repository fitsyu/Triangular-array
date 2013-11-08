#include <iostream>
#include <string>
#include <vector>
using namespace std;

//vector<vector< int>>  triangular_array(string orientation, int ordo)
void  triangular_array(string orientation, int ordo)
{
	vector<vector< int > >ta(ordo);
	int value;
	for (int row = 1; row <=3; ++row)
	{
		ta.resize(row);
		for (int col=1; col <= row; ++col)
		{
			ta.resize(col);
			cout << row << " " << col << " : "<< endl;
			cin >> value;
//			ta[row][col] = value;
		}
	}
}


int main()
{
	triangular_array("a", 3);
}
