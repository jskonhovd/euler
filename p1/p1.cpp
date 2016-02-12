#include <bits/stdc++.h>

using namespace std;

// cin >> input
// cout << output

int main() {
  int ret = 0;
  
  for(int i = 1; i < 1000; i++)
  {
    if(i%3 == 0 || i%5 == 0)
    {
      ret += i;
    }
  }

  cout << ret << endl;
  return 0;
}
