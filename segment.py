# Function: 分句、分词
# Author: ZhouYongJie
# Updated Date:
#   - 2021-05-19 添加英文分句方法

import re


class SegmentSentence:

    def __init__(self, line):
        """
        :param line: 字符串 str
        """
        pass
        self.line = line

    def get_sentence(self):
        """
        英文分句方法
        :return: 分句结果 list
        """
        pass
        pattern = re.compile(r"(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<! [a-z]\.)(?<![A-Z][a-z][a-z]\.)("
                             r"?<=\.|\?|!)\"*\s*\s*(?:\W*)([A-Z])")

        find_list = pattern.split(self.line)

        result_list = find_list[:1]
        for ids in range(1, len(find_list), 2):
            result_list.append(find_list[ids] + find_list[ids+1])

        return result_list


class SegmentWord:
    """
    分词
    """

    def __init__(self, line):
        self.line = line


if __name__ == "__main__":
    pass

    article = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam " \
              "Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. "
    # article = 'a'
    # article = '.'
    segment_mode = SegmentSentence(article)

    result = segment_mode.get_sentence()
    # print(result)
    for x in result:
        print(x)




